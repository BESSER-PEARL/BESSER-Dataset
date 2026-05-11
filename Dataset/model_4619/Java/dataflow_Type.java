





import java.util.List;
import java.util.ArrayList;

public class dataflow_Type  {

    private int bits;
    private String etype;





    private dataflow_Variable dataflow_variable;




    private dataflow_Buffer dataflow_buffer;


    public dataflow_Type(
        int bits,        String etype    ) {
        this.bits = bits;
        this.etype = etype;
    }


    public int getBits() {
        return bits;
    }

    public void setBits(int bits) {
        this.bits = bits;
    }
    public String getEtype() {
        return etype;
    }

    public void setEtype(String etype) {
        this.etype = etype;
    }

    public dataflow_Variable getDataflow_variable() {
        return dataflow_variable;
    }

    public void setDataflow_variable(dataflow_Variable dataflow_variable) {
        this.dataflow_variable = dataflow_variable;
    }
    public dataflow_Buffer getDataflow_buffer() {
        return dataflow_buffer;
    }

    public void setDataflow_buffer(dataflow_Buffer dataflow_buffer) {
        this.dataflow_buffer = dataflow_buffer;
    }

}