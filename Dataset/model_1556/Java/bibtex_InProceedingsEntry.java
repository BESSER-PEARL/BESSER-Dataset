





import java.util.List;
import java.util.ArrayList;

public class bibtex_InProceedingsEntry extends Entry {






    private bibtex_PageField bibtex_pagefield;




    private bibtex_AddressField bibtex_addressfield;




    private bibtex_SeriesField bibtex_seriesfield;


    public bibtex_InProceedingsEntry(
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
    public bibtex_AddressField getBibtex_addressfield() {
        return bibtex_addressfield;
    }

    public void setBibtex_addressfield(bibtex_AddressField bibtex_addressfield) {
        this.bibtex_addressfield = bibtex_addressfield;
    }
    public bibtex_SeriesField getBibtex_seriesfield() {
        return bibtex_seriesfield;
    }

    public void setBibtex_seriesfield(bibtex_SeriesField bibtex_seriesfield) {
        this.bibtex_seriesfield = bibtex_seriesfield;
    }

}