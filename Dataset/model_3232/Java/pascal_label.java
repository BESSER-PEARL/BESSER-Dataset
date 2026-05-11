





import java.util.List;
import java.util.ArrayList;

public class pascal_label  {

    private String number;





    private pascal_statement pascal_statement;


    public pascal_label(
        String number    ) {
        this.number = number;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public pascal_statement getPascal_statement() {
        return pascal_statement;
    }

    public void setPascal_statement(pascal_statement pascal_statement) {
        this.pascal_statement = pascal_statement;
    }

}