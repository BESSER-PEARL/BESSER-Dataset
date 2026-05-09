





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_PrePostOrBodyDeclCS extends CSTNode {

    private String kind;



    public ocl_cst_PrePostOrBodyDeclCS(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}