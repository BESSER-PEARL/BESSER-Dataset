





import java.util.List;
import java.util.ArrayList;

public class table_description_IntersectionMapping extends description_CellUpdater, description_TableMapping, description_StyleUpdater {

    private String semanticCandidatesExpression;
    private String preconditionExpression;
    private String lineFinderExpression;
    private String columnFinderExpression;
    private String domainClass;
    private boolean useDomainClass;
    private String labelExpression;





    private List<LineMapping> linemappings;




    private ColumnMapping columnmapping;


    public table_description_IntersectionMapping(
        String semanticCandidatesExpression,        String preconditionExpression,        String lineFinderExpression,        String columnFinderExpression,        String domainClass,        boolean useDomainClass,        String labelExpression    ) {
        super(
        );
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.lineFinderExpression = lineFinderExpression;
        this.columnFinderExpression = columnFinderExpression;
        this.domainClass = domainClass;
        this.useDomainClass = useDomainClass;
        this.labelExpression = labelExpression;
        this.linemappings = new ArrayList<>();
    }

    public table_description_IntersectionMapping(
        String semanticCandidatesExpression,        String preconditionExpression,        String lineFinderExpression,        String columnFinderExpression,        String domainClass,        boolean useDomainClass,        String labelExpression        ArrayList<LineMapping> linemappings    ) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.lineFinderExpression = lineFinderExpression;
        this.columnFinderExpression = columnFinderExpression;
        this.domainClass = domainClass;
        this.useDomainClass = useDomainClass;
        this.labelExpression = labelExpression;
        this.linemappings = linemappings;
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
    public String getLinefinderexpression() {
        return lineFinderExpression;
    }

    public void setLinefinderexpression(String lineFinderExpression) {
        this.lineFinderExpression = lineFinderExpression;
    }
    public String getColumnfinderexpression() {
        return columnFinderExpression;
    }

    public void setColumnfinderexpression(String columnFinderExpression) {
        this.columnFinderExpression = columnFinderExpression;
    }
    public String getDomainclass() {
        return domainClass;
    }

    public void setDomainclass(String domainClass) {
        this.domainClass = domainClass;
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