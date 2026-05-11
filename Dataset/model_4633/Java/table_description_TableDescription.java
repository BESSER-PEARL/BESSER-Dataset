





import java.util.List;
import java.util.ArrayList;

public class table_description_TableDescription extends description_EndUserDocumentedElement, description_DocumentedElement, description_RepresentationDescription {

    private String preconditionExpression;
    private String domainClass;
    private int initialHeaderColumnWidth;





    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;


    public table_description_TableDescription(
        String preconditionExpression,        String domainClass,        int initialHeaderColumnWidth    ) {
        super(
        );
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
    }

    public table_description_TableDescription(
        String preconditionExpression,        String domainClass,        int initialHeaderColumnWidth        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings    ) {
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
    }

    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
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