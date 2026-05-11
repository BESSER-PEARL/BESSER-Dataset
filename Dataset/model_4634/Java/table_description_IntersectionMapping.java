





import java.util.List;
import java.util.ArrayList;

public class table_description_IntersectionMapping extends description_CellUpdater, description_StyleUpdater, description_TableMapping {

    private String preconditionExpression;
    private String columnFinderExpression;
    private String labelExpression;
    private String semanticCandidatesExpression;
    private String domainClass;
    private String lineFinderExpression;
    private boolean useDomainClass;





    private ColumnMapping columnmapping;




    private List<LineMapping> linemappings;


    public table_description_IntersectionMapping(
        String preconditionExpression,        String columnFinderExpression,        String labelExpression,        String semanticCandidatesExpression,        String domainClass,        String lineFinderExpression,        boolean useDomainClass    ) {
        super(
        );
        this.preconditionExpression = preconditionExpression;
        this.columnFinderExpression = columnFinderExpression;
        this.labelExpression = labelExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
        this.lineFinderExpression = lineFinderExpression;
        this.useDomainClass = useDomainClass;
        this.linemappings = new ArrayList<>();
    }

    public table_description_IntersectionMapping(
        String preconditionExpression,        String columnFinderExpression,        String labelExpression,        String semanticCandidatesExpression,        String domainClass,        String lineFinderExpression,        boolean useDomainClass        ArrayList<LineMapping> linemappings    ) {
        this.preconditionExpression = preconditionExpression;
        this.columnFinderExpression = columnFinderExpression;
        this.labelExpression = labelExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
        this.lineFinderExpression = lineFinderExpression;
        this.useDomainClass = useDomainClass;
        this.linemappings = linemappings;
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
    public boolean getUsedomainclass() {
        return useDomainClass;
    }

    public void setUsedomainclass(boolean useDomainClass) {
        this.useDomainClass = useDomainClass;
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