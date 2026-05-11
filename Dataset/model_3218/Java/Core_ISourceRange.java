





import java.util.List;
import java.util.ArrayList;

public class Core_ISourceRange  {

    private String offset;
    private String length;





    private Core_IMember core_imember;




    private Core_ISourceReference core_isourcereference;




    private Core_IMember core_imember;


    public Core_ISourceRange(
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

    public Core_IMember getCore_imember() {
        return core_imember;
    }

    public void setCore_imember(Core_IMember core_imember) {
        this.core_imember = core_imember;
    }
    public Core_ISourceReference getCore_isourcereference() {
        return core_isourcereference;
    }

    public void setCore_isourcereference(Core_ISourceReference core_isourcereference) {
        this.core_isourcereference = core_isourcereference;
    }
    public Core_IMember getCore_imember() {
        return core_imember;
    }

    public void setCore_imember(Core_IMember core_imember) {
        this.core_imember = core_imember;
    }

}