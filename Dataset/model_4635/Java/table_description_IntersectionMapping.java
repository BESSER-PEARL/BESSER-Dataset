





import java.util.List;
import java.util.ArrayList;

public class table_description_IntersectionMapping extends description_StyleUpdater, description_TableMapping, description_CellUpdater {

    private String labelExpression;
    private String semanticCandidatesExpression;
    private String preconditionExpression;
    private String columnFinderExpression;
    private String domainClass;
    private boolean useDomainClass;
    private String lineFinderExpression;





    private ColumnMapping columnmapping;




    private List<LineMapping> linemappings;


    public table_description_IntersectionMapping(
        String labelExpression,        String semanticCandidatesExpression,        String preconditionExpression,        String columnFinderExpression,        String domainClass,        boolean useDomainClass,        String lineFinderExpression    ) {
        super(
        );
        this.labelExpression = labelExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.columnFinderExpression = columnFinderExpression;
        this.domainClass = domainClass;
        this.useDomainClass = useDomainClass;
        this.lineFinderExpression = lineFinderExpression;
        this.linemappings = new ArrayList<>();
    }

    public table_description_IntersectionMapping(
        String labelExpression,        String semanticCandidatesExpression,        String preconditionExpression,        String columnFinderExpression,        String domainClass,        boolean useDomainClass,        String lineFinderExpression        ArrayList<LineMapping> linemappings    ) {
        this.labelExpression = labelExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.preconditionExpression = preconditionExpression;
        this.columnFinderExpression = columnFinderExpression;
        this.domainClass = domainClass;
        this.useDomainClass = useDomainClass;
        this.lineFinderExpression = lineFinderExpression;
        this.linemappings = linemappings;
    }

    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
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
    public String getLinefinderexpression() {
        return lineFinderExpression;
    }

    public void setLinefinderexpression(String lineFinderExpression) {
        this.lineFinderExpression = lineFinderExpression;
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