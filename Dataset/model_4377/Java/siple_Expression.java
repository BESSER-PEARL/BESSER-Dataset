





import java.util.List;
import java.util.ArrayList;

public class siple_Expression extends Statement {

    private String Type;





    private siple_Write siple_write;




    private siple_While siple_while;




    private siple_If siple_if;


    public siple_Expression(
        String Type    ) {
        super(
        );
        this.Type = Type;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public siple_Write getSiple_write() {
        return siple_write;
    }

    public void setSiple_write(siple_Write siple_write) {
        this.siple_write = siple_write;
    }
    public siple_While getSiple_while() {
        return siple_while;
    }

    public void setSiple_while(siple_While siple_while) {
        this.siple_while = siple_while;
    }
    public siple_If getSiple_if() {
        return siple_if;
    }

    public void setSiple_if(siple_If siple_if) {
        this.siple_if = siple_if;
    }

}