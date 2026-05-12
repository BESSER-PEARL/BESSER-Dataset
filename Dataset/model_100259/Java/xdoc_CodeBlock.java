





import java.util.List;
import java.util.ArrayList;

public class xdoc_CodeBlock extends MarkUp {






    private xdoc_LangDef xdoc_langdef;




    private List<xdoc_EObject> xdoc_eobjects;


    public xdoc_CodeBlock(
    ) {
        super(
        );
        this.xdoc_eobjects = new ArrayList<>();
    }

    public xdoc_CodeBlock(
        ArrayList<xdoc_EObject> xdoc_eobjects    ) {
        this.xdoc_eobjects = xdoc_eobjects;
    }


    public xdoc_LangDef getXdoc_langdef() {
        return xdoc_langdef;
    }

    public void setXdoc_langdef(xdoc_LangDef xdoc_langdef) {
        this.xdoc_langdef = xdoc_langdef;
    }
    public List<xdoc_EObject> getXdoc_eobjects() {
        return xdoc_eobjects;
    }

    public void addXdoc_eobject(Xdoc_eobject xdoc_eobject) {
        this.xdoc_eobjects.add(xdoc_eobject);
    }

}