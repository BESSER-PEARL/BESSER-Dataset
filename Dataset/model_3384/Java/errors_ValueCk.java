





import java.util.List;
import java.util.ArrayList;

public class errors_ValueCk  {

    private String value;





    private errors_ColumnCk errors_columnck;


    public errors_ValueCk(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public errors_ColumnCk getErrors_columnck() {
        return errors_columnck;
    }

    public void setErrors_columnck(errors_ColumnCk errors_columnck) {
        this.errors_columnck = errors_columnck;
    }

}