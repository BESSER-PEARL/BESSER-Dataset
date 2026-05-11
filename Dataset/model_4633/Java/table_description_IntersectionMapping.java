





import java.util.List;
import java.util.ArrayList;

public class table_description_IntersectionMapping extends description_CellUpdater, description_StyleUpdater, description_TableMapping {

    private String labelExpression;
    private boolean useDomainClass;
    private String columnFinderExpression;
    private String lineFinderExpression;
    private String domainClass;
    private String preconditionExpression;
    private String semanticCandidatesExpression;





    private ColumnMapping columnmapping;




    private List<LineMapping> linemappings;


    public table_description_IntersectionMapping(
        String labelExpression,        boolean useDomainClass,        String columnFinderExpression,        String lineFinderExpression,        String domainClass,        String preconditionExpression,        String semanticCandidatesExpression    ) {
        super(
        );
        this.labelExpression = labelExpression;
        this.useDomainClass = useDomainClass;
        this.columnFinderExpression = columnFinderExpression;
        this.lineFinderExpression = lineFinderExpression;
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.linemappings = new ArrayList<>();
    }

    public table_description_IntersectionMapping(
        String labelExpression,        boolean useDomainClass,        String columnFinderExpression,        String lineFinderExpression,        String domainClass,        String preconditionExpression,        String semanticCandidatesExpression        ArrayList<LineMapping> linemappings    ) {
        this.labelExpression = labelExpression;
        this.useDomainClass = useDomainClass;
        this.columnFinderExpression = columnFinderExpression;
        this.lineFinderExpression = lineFinderExpression;
        this.domainClass = domainClass;
        this.preconditionExpression = preconditionExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.linemappings = linemappings;
    }

    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
    }
    public boolean getUsedomainclass() {
        return useDomainClass;
    }

    public void setUsedomainclass(boolean useDomainClass) {
        this.useDomainClass = useDomainClass;
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
    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
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