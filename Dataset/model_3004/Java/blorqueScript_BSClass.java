





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSClass  {

    private String name;





    private blorqueScript_BSFile blorquescript_bsfile;




    private blorqueScript_BSClass blorquescript_bsclass;


    public blorqueScript_BSClass(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public blorqueScript_BSFile getBlorquescript_bsfile() {
        return blorquescript_bsfile;
    }

    public void setBlorquescript_bsfile(blorqueScript_BSFile blorquescript_bsfile) {
        this.blorquescript_bsfile = blorquescript_bsfile;
    }
    public blorqueScript_BSClass getBlorquescript_bsclass() {
        return blorquescript_bsclass;
    }

    public void setBlorquescript_bsclass(blorqueScript_BSClass blorquescript_bsclass) {
        this.blorquescript_bsclass = blorquescript_bsclass;
    }

}