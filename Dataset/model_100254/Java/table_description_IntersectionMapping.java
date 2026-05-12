





import java.util.List;
import java.util.ArrayList;

public class table_description_IntersectionMapping extends description_CellUpdater, description_StyleUpdater, description_TableMapping {

    private String labelExpression;
    private String domainClass;
    private String columnFinderExpression;
    private String lineFinderExpression;
    private boolean useDomainClass;
    private String semanticCandidatesExpression;
    private String preconditionExpression;





    private ColumnMapping columnmapping;




    private List<LineMapping> linemappings;


    public table_description_IntersectionMapping(
        String labelExpression,        String domainClass,        String columnFinderExpression,        String lineFinderExpression,        boolean useDomainClass,        String semanticCandidatesExpression,        String preconditionExpression    ) {
        super(
        );
        this.labelExpression = labelExpression;
        this.domainClass = domainClass;
        this.columnFinderExpression = columnFinderExpression;
        this.lineFinderExpression = lineFinderExpression;
        this.useDomainClass = useDomainClass;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.linemappings = new ArrayList<>();
    }

    public table_description_IntersectionMapping(
        String labelExpression,        String domainClass,        String columnFinderExpression,        String lineFinderExpression,        boolean useDomainClass,        String semanticCandidatesExpression,        String preconditionExpression        ArrayList<LineMapping> linemappings    ) {
        this.labelExpression = labelExpression;
        this.domainClass = domainClass;
        this.columnFinderExpression = columnFinderExpression;
        this.lineFinderExpression = lineFinderExpression;
        this.useDomainClass = useDomainClass;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.linemappings = linemappings;
    }

    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getColumnfinderexpression() {
        return columnFinderExpression;
    }

    public void setColumnfinderexpression(String columnFinderExpression) {
        this.columnFinderExpression = columnFinderExpression;
    }
    public String getLinefinderexpression() {
        return lineFinderExpression;
    }

    public void setLinefinderexpression(String lineFinderExpression) {
        this.lineFinderExpression = lineFinderExpression;
    }
    public boolean getUsedomainclass() {
        return useDomainClass;
    }

    public void setUsedomainclass(boolean useDomainClass) {
        this.useDomainClass = useDomainClass;
    }
    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }

    public ColumnMapping getColumnmapping() {
        return columnmapping;
    }

    public void setColumnmapping(ColumnMapping columnmapping) {
        this.columnmapping = columnmapping;
    }
    public List<LineMapping> getLinemappings() {
        return linemappings;
    }

    public void addLinemapping(Linemapping linemapping) {
        this.linemappings.add(linemapping);
    }

}