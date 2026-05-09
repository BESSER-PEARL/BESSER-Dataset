





import java.util.List;
import java.util.ArrayList;

public class drn_Definition  {

    private String int;
    private String text;
    private String bool;
    private String real;





    private drn_Declaration drn_declaration;


    public drn_Definition(
        String int,        String text,        String bool,        String real    ) {
        this.int = int;
        this.text = text;
        this.bool = bool;
        this.real = real;
    }


    public String getInt() {
        return int;
    }

    public void setInt(String int) {
        this.int = int;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getBool() {
        return bool;
    }

    public void setBool(String bool) {
        this.bool = bool;
    }
    public String getReal() {
        return real;
    }

    public void setReal(String real) {
        this.real = real;
    }

    public drn_Declaration getDrn_declaration() {
        return drn_declaration;
    }

    public void setDrn_declaration(drn_Declaration drn_declaration) {
        this.drn_declaration = drn_declaration;
    }

}