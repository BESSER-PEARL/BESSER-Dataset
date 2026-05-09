





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ISourceRange  {

    private String offset;
    private String length;





    private JDTAST_IMember jdtast_imember;




    private JDTAST_ISourceReference jdtast_isourcereference;




    private JDTAST_IMember jdtast_imember;


    public JDTAST_ISourceRange(
        String offset,        String length    ) {
        this.offset = offset;
        this.length = length;
    }


    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public String getLength() {
        return length;
    }

    public void setLength(String length) {
        this.length = length;
    }

    public JDTAST_IMember getJdtast_imember() {
        return jdtast_imember;
    }

    public void setJdtast_imember(JDTAST_IMember jdtast_imember) {
        this.jdtast_imember = jdtast_imember;
    }
    public JDTAST_ISourceReference getJdtast_isourcereference() {
        return jdtast_isourcereference;
    }

    public void setJdtast_isourcereference(JDTAST_ISourceReference jdtast_isourcereference) {
        this.jdtast_isourcereference = jdtast_isourcereference;
    }
    public JDTAST_IMember getJdtast_imember() {
        return jdtast_imember;
    }

    public void setJdtast_imember(JDTAST_IMember jdtast_imember) {
        this.jdtast_imember = jdtast_imember;
    }

}