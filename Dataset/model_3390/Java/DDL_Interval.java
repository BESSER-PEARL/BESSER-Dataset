





import java.util.List;
import java.util.ArrayList;

public class DDL_Interval extends Type {

    private int precision1;
    private String field1;
    private int precision2;
    private String field2;



    public DDL_Interval(
        int precision1,        String field1,        int precision2,        String field2    ) {
        super(
        );
        this.precision1 = precision1;
        this.field1 = field1;
        this.precision2 = precision2;
        this.field2 = field2;
    }


    public int getPrecision1() {
        return precision1;
    }

    public void setPrecision1(int precision1) {
        this.precision1 = precision1;
    }
    public String getField1() {
        return field1;
    }

    public void setField1(String field1) {
        this.field1 = field1;
    }
    public int getPrecision2() {
        return precision2;
    }

    public void setPrecision2(int precision2) {
        this.precision2 = precision2;
    }
    public String getField2() {
        return field2;
    }

    public void setField2(String field2) {
        this.field2 = field2;
    }


}