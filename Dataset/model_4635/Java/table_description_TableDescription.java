





import java.util.List;
import java.util.ArrayList;

public class table_description_TableDescription extends description_DocumentedElement, description_EndUserDocumentedElement, description_RepresentationDescription {

    private String domainClass;
    private int initialHeaderColumnWidth;
    private String preconditionExpression;





    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;


    public table_description_TableDescription(
        String domainClass,        int initialHeaderColumnWidth,        String preconditionExpression    ) {
        super(
        );
        this.domainClass = domainClass;
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
        this.preconditionExpression = preconditionExpression;
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
    }

    public table_description_TableDescription(
        String domainClass,        int initialHeaderColumnWidth,        String preconditionExpression        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings    ) {
        this.domainClass = domainClass;
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
        this.preconditionExpression = preconditionExpression;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
    }

    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public int getInitialheadercolumnwidth() {
        return initialHeaderColumnWidth;
    }

    public void setInitialheadercolumnwidth(int initialHeaderColumnWidth) {
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
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