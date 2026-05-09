





import java.util.List;
import java.util.ArrayList;

public class easyflow_Tool  {

    private String toolName;
    private String refData;
    private String subCmd;
    private String type;
    private String subCmdPrefix;
    private String category;
    private String source;
    private String pattern;





    private easyflow_Interpreter easyflow_interpreter;




    private List<easyflow_CommandArgument> easyflow_commandarguments;




    private List<easyflow_CommandArgument> easyflow_commandarguments;




    private easyflow_Task easyflow_task;




    private List<easyflow_CommandArgument> easyflow_commandarguments;




    private List<easyflow_CommandArgument> easyflow_commandarguments;




    private easyflow_StringToToolMap easyflow_stringtotoolmap;


    public easyflow_Tool(
        String toolName,        String refData,        String subCmd,        String type,        String subCmdPrefix,        String category,        String source,        String pattern    ) {
        this.toolName = toolName;
        this.refData = refData;
        this.subCmd = subCmd;
        this.type = type;
        this.subCmdPrefix = subCmdPrefix;
        this.category = category;
        this.source = source;
        this.pattern = pattern;
        this.easyflow_commandarguments = new ArrayList<>();
        this.easyflow_commandarguments = new ArrayList<>();
        this.easyflow_commandarguments = new ArrayList<>();
        this.easyflow_commandarguments = new ArrayList<>();
    }

    public easyflow_Tool(
        String toolName,        String refData,        String subCmd,        String type,        String subCmdPrefix,        String category,        String source,        String pattern        ArrayList<easyflow_CommandArgument> easyflow_commandarguments,        ArrayList<easyflow_CommandArgument> easyflow_commandarguments,        ArrayList<easyflow_CommandArgument> easyflow_commandarguments,        ArrayList<easyflow_CommandArgument> easyflow_commandarguments    ) {
        this.toolName = toolName;
        this.refData = refData;
        this.subCmd = subCmd;
        this.type = type;
        this.subCmdPrefix = subCmdPrefix;
        this.category = category;
        this.source = source;
        this.pattern = pattern;
        this.easyflow_commandarguments = easyflow_commandarguments;
        this.easyflow_commandarguments = easyflow_commandarguments;
        this.easyflow_commandarguments = easyflow_commandarguments;
        this.easyflow_commandarguments = easyflow_commandarguments;
    }

    public String getToolname() {
        return toolName;
    }

    public void setToolname(String toolName) {
        this.toolName = toolName;
    }
    public String getRefdata() {
        return refData;
    }

    public void setRefdata(String refData) {
        this.refData = refData;
    }
    public String getSubcmd() {
        return subCmd;
    }

    public void setSubcmd(String subCmd) {
        this.subCmd = subCmd;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSubcmdprefix() {
        return subCmdPrefix;
    }

    public void setSubcmdprefix(String subCmdPrefix) {
        this.subCmdPrefix = subCmdPrefix;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }

    public easyflow_Interpreter getEasyflow_interpreter() {
        return easyflow_interpreter;
    }

    public void setEasyflow_interpreter(easyflow_Interpreter easyflow_interpreter) {
        this.easyflow_interpreter = easyflow_interpreter;
    }
    public List<easyflow_CommandArgument> getEasyflow_commandarguments() {
        return easyflow_commandarguments;
    }

    public void addEasyflow_commandargument(Easyflow_commandargument easyflow_commandargument) {
        this.easyflow_commandarguments.add(easyflow_commandargument);
    }
    public List<easyflow_CommandArgument> getEasyflow_commandarguments() {
        return easyflow_commandarguments;
    }

    public void addEasyflow_commandargument(Easyflow_commandargument easyflow_commandargument) {
        this.easyflow_commandarguments.add(easyflow_commandargument);
    }
    public easyflow_Task getEasyflow_task() {
        return easyflow_task;
    }

    public void setEasyflow_task(easyflow_Task easyflow_task) {
        this.easyflow_task = easyflow_task;
    }
    public List<easyflow_CommandArgument> getEasyflow_commandarguments() {
        return easyflow_commandarguments;
    }

    public void addEasyflow_commandargument(Easyflow_commandargument easyflow_commandargument) {
        this.easyflow_commandarguments.add(easyflow_commandargument);
    }
    public List<easyflow_CommandArgument> getEasyflow_commandarguments() {
        return easyflow_commandarguments;
    }

    public void addEasyflow_commandargument(Easyflow_commandargument easyflow_commandargument) {
        this.easyflow_commandarguments.add(easyflow_commandargument);
    }
    public easyflow_StringToToolMap getEasyflow_stringtotoolmap() {
        return easyflow_stringtotoolmap;
    }

    public void setEasyflow_stringtotoolmap(easyflow_StringToToolMap easyflow_stringtotoolmap) {
        this.easyflow_stringtotoolmap = easyflow_stringtotoolmap;
    }

}