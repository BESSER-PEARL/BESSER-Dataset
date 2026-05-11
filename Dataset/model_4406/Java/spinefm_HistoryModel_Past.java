





import java.util.List;
import java.util.ArrayList;

public class spinefm_HistoryModel_Past  {

    private String description;
    private String id;
    private String modelPath;
    private String rootPath;





    private List<Step> steps;




    private List<LocalContext> localcontexts;


    public spinefm_HistoryModel_Past(
        String description,        String id,        String modelPath,        String rootPath    ) {
        this.description = description;
        this.id = id;
        this.modelPath = modelPath;
        this.rootPath = rootPath;
        this.steps = new ArrayList<>();
        this.localcontexts = new ArrayList<>();
    }

    public spinefm_HistoryModel_Past(
        String description,        String id,        String modelPath,        String rootPath        ArrayList<Step> steps,        ArrayList<LocalContext> localcontexts    ) {
        this.description = description;
        this.id = id;
        this.modelPath = modelPath;
        this.rootPath = rootPath;
        this.steps = steps;
        this.localcontexts = localcontexts;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getModelpath() {
        return modelPath;
    }

    public void setModelpath(String modelPath) {
        this.modelPath = modelPath;
    }
    public String getRootpath() {
        return rootPath;
    }

    public void setRootpath(String rootPath) {
        this.rootPath = rootPath;
    }

    public List<Step> getSteps() {
        return steps;
    }

    public void addStep(Step step) {
        this.steps.add(step);
    }
    public List<LocalContext> getLocalcontexts() {
        return localcontexts;
    }

    public void addLocalcontext(Localcontext localcontext) {
        this.localcontexts.add(localcontext);
    }

}