## dungeon.vxml

```mermaid
flowchart LR

    A[Start - Wake up in dark room]
    A --> B
    B{Choose}
    B -- sleep--> D
  subgraph wa1[Wakeup Scene]

    D[End: Wake in own bed]
    D ==> End1[Exit]
    V[Too many noinput/nomatch → Exit]
  end
    B --look around--> F
    End1 ~~~ P
    F[Explore room]
%%   subgraph re1[Room Exploration]
    %% G{Choose: door or table}
    W[Too many noinput/nomatch → Exit]

    I --> J{Has key?}
    H --> M{Has key?}
    %% G --> I
    %% G --> H
    F --> I
    F --> H
    
    subgraph Table Interaction
        I[Inspect Table]
        J -->|false| K[Find key, set hasKey = true]

        J -->|true| L[Table empty]
    end

  subgraph Door Interaction
    H[Inspect Door]
    M -->|false| N[Door is locked]

    M -->|true| O[Door opens to corridor]
    
  end
%%   end
    O --> P
    %% F --> G

    K --> F
    L --> F

    N --> F

  subgraph Corridor
    P{Choose direction}
    %% P --> Q[Left]
    %% Q --> R[Dead end, return]
    P --Left--> R[Dead end, return]
    R --> P

    %% P --> S[Right]
    %% S --> T[Freedom: new room]
    P --Right--> T[Freedom: new room]
    T --> U[Load puzzle.vxml]
    X[Too many noinput/nomatch → Exit]
  end


  U --> End2[Next VXML]

```

## dungeon.vxml (2nd option)

```mermaid
flowchart LR

  subgraph wa1[Wakeup Scene]
    A[Start - Wake up in dark room]
    A --> B
    B{Choose}

    D[End: Wake in own bed]
    D ==> End1[Exit]
    V[Too many noinput/nomatch → Exit]
  end
    B -- sleep--> D
    B --look around--> F
    End1 ~~~ P
    subgraph Exploration
    F[Explore room]
%%   subgraph re1[Room Exploration]
    %% G{Choose: door or table}
    W[Too many noinput/nomatch → Exit]

    I --> J{Has key?}
    H --> M{Has key?}
    %% G --> I
    %% G --> H
    F --> I
    F --> H
    
    subgraph Table Interaction
        I[Inspect Table]
        J -->|false| K[Find key, set hasKey = true]

        J -->|true| L[Table empty]
    end

  subgraph Door Interaction
    H[Inspect Door]
    M -->|false| N[Door is locked]

    M -->|true| O[Door opens to corridor]
    
  end
    end
%%   end
    O --> P
    %% F --> G

    K --> F
    L --> F

    N --> F

  subgraph Corridor
    P{Choose direction}
    %% P --> Q[Left]
    %% Q --> R[Dead end, return]
    P --Left--> R[Dead end, return]
    R --> P

    %% P --> S[Right]
    %% S --> T[Freedom: new room]
    P --Right--> T[Freedom: new room]
    T --> U[Load puzzle.vxml]
    X[Too many noinput/nomatch → Exit]
  end

    F~~~P
  U --> End2[Next VXML]

```

## puzzle.vxml

```mermaid

flowchart LR

  A[Entry Point] 
  A@{ shape: circle }
    B[Main Choice Menu]
    G[Recall Memory]
    G --> B
  A --> B
B e3@<==> C
B e2@==> D
B e1@==> E
B e5@==> F
%%   subgraph Exploration
    C[Inspect Table<br>_no clues_]
    %% C --> B

    subgraph Paintings
    Eretp[Return to Menu]
    D[Painting Overview]
    D --> D1[Choose Painting]

    D1 --> D2[East Wall<br>King Alric, 4]
    D2 -->D12[/Set mem_east = true/] --> Eretp

    D1 --> D3[North Wall<br>Queen Berena, 9]
    D3 -->D11[/Set mem_north = true/] -->Eretp

    D1 --> D4[West Wall<br>Prince Cedric, 2]
    D4 --> D10[/Set mem_west = true/] -->Eretp
    Eretp e7@-.-> D
    %% D1 --> B
    end

    subgraph Bookshelf
        Eret[Return to Menu]
        E[Inspect Bookshelf]
        E --> E1[Choose Book]

        E1 --> E2[Cooking for Nobles]
        E2 --> E11>_no clue_] --> Eret

        E1 --> E3[Legends of the Realm]
        E3 --> E12>_no clue_] -->Eret

        E1 --> E4[Royal Bloodlines]
        E4 -->E10[/set knowsOrder = true/]--> Eret
        Eret e8@-.-> E        

        %% E1 --> B
    end
%%   end
    D -.-> G
    E -.-> G


  subgraph Door Puzzle
    F[Check Door]
    F --> F1[Enter Code]

    F1 --> F2[Code is 4 9 2  - Success]

    F1 --> F3[Code _order_ is wrong]
    F3 --> F11

    F1 --> F4[Incorrect Code<br>_doesn't contain 2,4,9_]
    F4 -->F10{mem_east<br>mem_north<br>mem_west<br>all true} --> |true|F11[Return to Menu] e9@-.->F
    
    F2 e10@==> I[Exit - Puzzle Solved]
  end
    F10 -->|Else| B
    F -.-> G
    B e6@==> H[Quit]


    classDef mainMenu stroke:red
    classDef menuReturn stroke:orange
    classDef exit stroke:lightgreen, animate: true 
    class e1 mainMenu
    class e2 mainMenu
    class e3 mainMenu
    class e4 mainMenu
    class e5 mainMenu
    class e6 exit
    class e10 exit
    e10@{ animate: true }
    class e7 menuReturn
    class e8 menuReturn
    class e9 menuReturn

```