





import java.util.List;
import java.util.ArrayList;

public class pycom_ParameterType  {

    private String text;
    private int number;





    private pycom_Import pycom_import;


    public pycom_ParameterType(
        String text,        int number    ) {
        this.text = text;
        this.number = number;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public pycom_Import getPycom_import() {
        return pycom_import;
    }

    public void setPycom_import(pycom_Import pycom_import) {
        this.pycom_import = pycom_import;
    }

}