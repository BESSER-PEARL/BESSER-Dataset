





import java.util.List;
import java.util.ArrayList;

public class table_description_TableDescription extends description_EndUserDocumentedElement, description_DocumentedElement, description_RepresentationDescription {

    private int initialHeaderColumnWidth;
    private String preconditionExpression;
    private String domainClass;





    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;


    public table_description_TableDescription(
        int initialHeaderColumnWidth,        String preconditionExpression,        String domainClass    ) {
        super(
        );
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
    }

    public table_description_TableDescription(
        int initialHeaderColumnWidth,        String preconditionExpression,        String domainClass        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings    ) {
        this.initialHeaderColumnWidth = initialHeaderColumnWidth;
        this.preconditionExpression = preconditionExpression;
        this.domainClass = domainClass;
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