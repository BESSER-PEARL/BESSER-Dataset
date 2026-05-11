





import java.util.List;
import java.util.ArrayList;

public class table_description_LineMapping extends description_StyleUpdater, description_TableMapping {

    private String headerLabelExpression;
    private String semanticCandidatesExpression;
    private String domainClass;





    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;




    private List<CreateLineTool> createlinetools;




    private List<LineMapping> linemappings;


    public table_description_LineMapping(
        String headerLabelExpression,        String semanticCandidatesExpression,        String domainClass    ) {
        super(
        );
        this.headerLabelExpression = headerLabelExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
        this.createlinetools = new ArrayList<>();
        this.linemappings = new ArrayList<>();
    }

    public table_description_LineMapping(
        String headerLabelExpression,        String semanticCandidatesExpression,        String domainClass        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings,        ArrayList<CreateLineTool> createlinetools,        ArrayList<LineMapping> linemappings    ) {
        this.headerLabelExpression = headerLabelExpression;
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
        this.createlinetools = createlinetools;
        this.linemappings = linemappings;
    }

    public String getHeaderlabelexpression() {
        return headerLabelExpression;
    }

    public void setHeaderlabelexpression(String headerLabelExpression) {
        this.headerLabelExpression = headerLabelExpression;
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
    public List<CreateLineTool> getCreatelinetools() {
        return createlinetools;
    }

    public void addCreatelinetool(Createlinetool createlinetool) {
        this.createlinetools.add(createlinetool);
    }
    public List<LineMapping> getLinemappings() {
        return linemappings;
    }

    public void addLinemapping(Linemapping linemapping) {
        this.linemappings.add(linemapping);
    }

}