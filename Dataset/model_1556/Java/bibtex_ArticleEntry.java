





import java.util.List;
import java.util.ArrayList;

public class bibtex_ArticleEntry extends Entry {






    private bibtex_PageField bibtex_pagefield;


    public bibtex_ArticleEntry(
    ) {
        super(
        );
    }



    public bibtex_PageField getBibtex_pagefield() {
        return bibtex_pagefield;
    }

    public void setBibtex_pagefield(bibtex_PageField bibtex_pagefield) {
        this.bibtex_pagefield = bibtex_pagefield;
    }

}