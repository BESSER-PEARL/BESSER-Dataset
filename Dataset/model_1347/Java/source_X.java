





import java.util.List;
import java.util.ArrayList;

public class source_X extends SElement {

    private boolean isA1;
    private boolean isA2;
    private String name;





    private source_SRoot source_sroot;


    public source_X(
        boolean isA1,        boolean isA2,        String name    ) {
        super(
        );
        this.isA1 = isA1;
        this.isA2 = isA2;
        this.name = name;
    }


    public boolean getIsa1() {
        return isA1;
    }

    public void setIsa1(boolean isA1) {
        this.isA1 = isA1;
    }
    public boolean getIsa2() {
        return isA2;
    }

    public void setIsa2(boolean isA2) {
        this.isA2 = isA2;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public source_SRoot getSource_sroot() {
        return source_sroot;
    }

    public void setSource_sroot(source_SRoot source_sroot) {
        this.source_sroot = source_sroot;
    }

}