





import java.util.List;
import java.util.ArrayList;

public class table_description_TableDescription extends description_DocumentedElement, description_RepresentationDescription, description_EndUserDocumentedElement {

    private int initialHeaderColumnWidth;
    private String domainClass;
    private String preconditionExpression;





    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;


    public table_description_TableDescription(
        int initialHeaderColumnWidth,        String domainClass,        String preconditionExpression    ) {
        super(
        );
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
    }

    public table_description_TableDescription(
        int initialHeaderColumnWidth,        String domainClass,        String preconditionExpression        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings    ) {
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
    }

    public int getInitialheadercolumnwidth() {
        return initialHeaderColumnWidth;
    }

    public void setInitialheadercolumnwidth(int initialHeaderColumnWidth) {
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }

    public List<LineMapping> getLinemappings() {
        return linemappings;
    }

    public void addLinemapping(Linemapping linemapping) {
        this.linemappings.add(linemapping);
    }
    public List<LineMapping> getLinemappings() {
        return linemappings;
    }

    public void addLinemapping(Linemapping linemapping) {
        this.linemappings.add(linemapping);
    }
    public List<LineMapping> getLinemappings() {
        return linemappings;
    }

    public void addLinemapping(Linemapping linemapping) {
        this.linemappings.add(linemapping);
    }

}