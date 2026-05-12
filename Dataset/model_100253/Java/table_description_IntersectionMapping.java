





import java.util.List;
import java.util.ArrayList;

public class table_description_IntersectionMapping extends description_CellUpdater, description_TableMapping, description_StyleUpdater {

    private String columnFinderExpression;
    private String semanticCandidatesExpression;
    private String domainClass;
    private String lineFinderExpression;
    private String preconditionExpression;
    private boolean useDomainClass;
    private String labelExpression;





    private List<LineMapping> linemappings;




    private ColumnMapping columnmapping;


    public table_description_IntersectionMapping(
        String columnFinderExpression,        String semanticCandidatesExpression,        String domainClass,        String lineFinderExpression,        String preconditionExpression,        boolean useDomainClass,        String labelExpression    ) {
        super(
        );
        this.columnFinderExpression = columnFinderExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
        this.lineFinderExpression = lineFinderExpression;
        this.preconditionExpression = preconditionExpression;
        this.useDomainClass = useDomainClass;
        this.labelExpression = labelExpression;
        this.linemappings = new ArrayList<>();
    }

    public table_description_IntersectionMapping(
        String columnFinderExpression,        String semanticCandidatesExpression,        String domainClass,        String lineFinderExpression,        String preconditionExpression,        boolean useDomainClass,        String labelExpression        ArrayList<LineMapping> linemappings    ) {
        this.columnFinderExpression = columnFinderExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
        this.lineFinderExpression = lineFinderExpression;
        this.preconditionExpression = preconditionExpression;
        this.useDomainClass = useDomainClass;
        this.labelExpression = labelExpression;
        this.linemappings = linemappings;
    }

    public String getColumnfinderexpression() {
        return columnFinderExpression;
    }

    public void setColumnfinderexpression(String columnFinderExpression) {
        this.columnFinderExpression = columnFinderExpression;
    }
    public String getSemanticcandidatesexpression() {
        return semanticCandidatesExpression;
    }

    public void setSemanticcandidatesexpression(String semanticCandidatesExpression) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
    }
    public String getLinefinderexpression() {
        return lineFinderExpression;
    }

    public void setLinefinderexpression(String lineFinderExpression) {
        this.lineFinderExpression = lineFinderExpression;
    }
    public String getPreconditionexpression() {
        return preconditionExpression;
    }

    public void setPreconditionexpression(String preconditionExpression) {
        this.preconditionExpression = preconditionExpression;
    }
    public boolean getUsedomainclass() {
        return useDomainClass;
    }

    public void setUsedomainclass(boolean useDomainClass) {
        this.useDomainClass = useDomainClass;
    }
    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
    }

    public List<LineMapping> getLinemappings() {
        return linemappings;
    }

    public void addLinemapping(Linemapping linemapping) {
        this.linemappings.add(linemapping);
    }
    public ColumnMapping getColumnmapping() {
        return columnmapping;
    }

    public void setColumnmapping(ColumnMapping columnmapping) {
        this.columnmapping = columnmapping;
    }

}