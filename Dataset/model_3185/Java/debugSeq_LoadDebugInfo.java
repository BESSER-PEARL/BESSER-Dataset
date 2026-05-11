





import java.util.List;
import java.util.ArrayList;

public class debugSeq_LoadDebugInfo extends Expression {

    private String path;



    public debugSeq_LoadDebugInfo(
        String path    ) {
        super(
        );
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}