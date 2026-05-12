





import java.util.List;
import java.util.ArrayList;

public class table_description_LineMapping extends description_StyleUpdater, description_TableMapping {

    private String semanticCandidatesExpression;
    private String domainClass;
    private String headerLabelExpression;





    private List<LineMapping> linemappings;




    private List<LineMapping> linemappings;




    private DeleteLineTool deletelinetool;




    private List<LineMapping> linemappings;




    private List<CreateLineTool> createlinetools;




    private List<LineMapping> linemappings;


    public table_description_LineMapping(
        String semanticCandidatesExpression,        String domainClass,        String headerLabelExpression    ) {
        super(
        );
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
        this.headerLabelExpression = headerLabelExpression;
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
        this.linemappings = new ArrayList<>();
        this.createlinetools = new ArrayList<>();
        this.linemappings = new ArrayList<>();
    }

    public table_description_LineMapping(
        String semanticCandidatesExpression,        String domainClass,        String headerLabelExpression        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings,        ArrayList<LineMapping> linemappings,        ArrayList<CreateLineTool> createlinetools,        ArrayList<LineMapping> linemappings    ) {
        this.semanticCandidatesExpression = semanticCandidatesExpression;
        this.domainClass = domainClass;
        this.headerLabelExpression = headerLabelExpression;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
        this.linemappings = linemappings;
        this.createlinetools = createlinetools;
        this.linemappings = linemappings;
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
    public String getHeaderlabelexpression() {
        return headerLabelExpression;
    }

    public void setHeaderlabelexpression(String headerLabelExpression) {
        this.headerLabelExpression = headerLabelExpression;
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
    public DeleteLineTool getDeletelinetool() {
        return deletelinetool;
    }

    public void setDeletelinetool(DeleteLineTool deletelinetool) {
        this.deletelinetool = deletelinetool;
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