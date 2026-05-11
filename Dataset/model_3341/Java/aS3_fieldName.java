





import java.util.List;
import java.util.ArrayList;

public class aS3_fieldName  {

    private String name;
    private String number;





    private aS3_literalField as3_literalfield;




    private aS3_identi as3_identi;


    public aS3_fieldName(
        String name,        String number    ) {
        this.name = name;
        this.number = number;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public aS3_literalField getAs3_literalfield() {
        return as3_literalfield;
    }

    public void setAs3_literalfield(aS3_literalField as3_literalfield) {
        this.as3_literalfield = as3_literalfield;
    }
    public aS3_identi getAs3_identi() {
        return as3_identi;
    }

    public void setAs3_identi(aS3_identi as3_identi) {
        this.as3_identi = as3_identi;
    }

}