





import java.util.List;
import java.util.ArrayList;

public class sexec_StateVector  {

    private int size;
    private int offset;





    private sexec_ExecutionRegion sexec_executionregion;


    public sexec_StateVector(
        int size,        int offset    ) {
        this.size = size;
        this.offset = offset;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }

    public sexec_ExecutionRegion getSexec_executionregion() {
        return sexec_executionregion;
    }

    public void setSexec_executionregion(sexec_ExecutionRegion sexec_executionregion) {
        this.sexec_executionregion = sexec_executionregion;
    }

}