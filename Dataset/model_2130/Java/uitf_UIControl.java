





import java.util.List;
import java.util.ArrayList;

public class uitf_UIControl  {

    private String id;





    private uitf_UISUT uitf_uisut;




    private uitf_Variable uitf_variable;


    public uitf_UIControl(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public uitf_UISUT getUitf_uisut() {
        return uitf_uisut;
    }

    public void setUitf_uisut(uitf_UISUT uitf_uisut) {
        this.uitf_uisut = uitf_uisut;
    }
    public uitf_Variable getUitf_variable() {
        return uitf_variable;
    }

    public void setUitf_variable(uitf_Variable uitf_variable) {
        this.uitf_variable = uitf_variable;
    }

}