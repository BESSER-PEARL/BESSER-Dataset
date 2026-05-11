





import java.util.List;
import java.util.ArrayList;

public class architecture_Type extends AnalysedElement {

    private boolean binary;
    private boolean source;
    private String qualifiedName;



    public architecture_Type(
        boolean binary,        boolean source,        String qualifiedName    ) {
        super(
        );
        this.binary = binary;
        this.source = source;
        this.qualifiedName = qualifiedName;
    }


    public boolean getBinary() {
        return binary;
    }

    public void setBinary(boolean binary) {
        this.binary = binary;
    }
    public boolean getSource() {
        return source;
    }

    public void setSource(boolean source) {
        this.source = source;
    }
    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }


}