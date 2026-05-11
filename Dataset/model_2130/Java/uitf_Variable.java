





import java.util.List;
import java.util.ArrayList;

public class uitf_Variable  {

    private String id;





    private uitf_Statement uitf_statement;




    private uitf_UISUT uitf_uisut;


    public uitf_Variable(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public uitf_Statement getUitf_statement() {
        return uitf_statement;
    }

    public void setUitf_statement(uitf_Statement uitf_statement) {
        this.uitf_statement = uitf_statement;
    }
    public uitf_UISUT getUitf_uisut() {
        return uitf_uisut;
    }

    public void setUitf_uisut(uitf_UISUT uitf_uisut) {
        this.uitf_uisut = uitf_uisut;
    }

}