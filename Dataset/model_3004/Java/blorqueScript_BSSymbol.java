





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSSymbol  {

    private String name;
    private String pType;





    private blorqueScript_BSClass blorquescript_bsclass;


    public blorqueScript_BSSymbol(
        String name,        String pType    ) {
        this.name = name;
        this.pType = pType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPtype() {
        return pType;
    }

    public void setPtype(String pType) {
        this.pType = pType;
    }

    public blorqueScript_BSClass getBlorquescript_bsclass() {
        return blorquescript_bsclass;
    }

    public void setBlorquescript_bsclass(blorqueScript_BSClass blorquescript_bsclass) {
        this.blorquescript_bsclass = blorquescript_bsclass;
    }

}