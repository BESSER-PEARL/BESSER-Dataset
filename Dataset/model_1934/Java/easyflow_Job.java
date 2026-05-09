





import java.util.List;
import java.util.ArrayList;

public class easyflow_Job  {

    private String exe;
    private String dependencies;
    private String interpreterOption;
    private String subCmd;
    private String inputArgs;
    private String source;
    private String targetPlatformOptions;
    private String genericArgs;
    private String staticArgs;
    private String targetPlatform;
    private String targets;
    private String outputArgs;
    private String name;





    private easyflow_EasyFlowMetadata easyflow_easyflowmetadata;


    public easyflow_Job(
        String exe,        String dependencies,        String interpreterOption,        String subCmd,        String inputArgs,        String source,        String targetPlatformOptions,        String genericArgs,        String staticArgs,        String targetPlatform,        String targets,        String outputArgs,        String name    ) {
        this.exe = exe;
        this.dependencies = dependencies;
        this.interpreterOption = interpreterOption;
        this.subCmd = subCmd;
        this.inputArgs = inputArgs;
        this.source = source;
        this.targetPlatformOptions = targetPlatformOptions;
        this.genericArgs = genericArgs;
        this.staticArgs = staticArgs;
        this.targetPlatform = targetPlatform;
        this.targets = targets;
        this.outputArgs = outputArgs;
        this.name = name;
    }


    public String getExe() {
        return exe;
    }

    public void setExe(String exe) {
        this.exe = exe;
    }
    public String getDependencies() {
        return dependencies;
    }

    public void setDependencies(String dependencies) {
        this.dependencies = dependencies;
    }
    public String getInterpreteroption() {
        return interpreterOption;
    }

    public void setInterpreteroption(String interpreterOption) {
        this.interpreterOption = interpreterOption;
    }
    public String getSubcmd() {
        return subCmd;
    }

    public void setSubcmd(String subCmd) {
        this.subCmd = subCmd;
    }
    public String getInputargs() {
        return inputArgs;
    }

    public void setInputargs(String inputArgs) {
        this.inputArgs = inputArgs;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTargetplatformoptions() {
        return targetPlatformOptions;
    }

    public void setTargetplatformoptions(String targetPlatformOptions) {
        this.targetPlatformOptions = targetPlatformOptions;
    }
    public String getGenericargs() {
        return genericArgs;
    }

    public void setGenericargs(String genericArgs) {
        this.genericArgs = genericArgs;
    }
    public String getStaticargs() {
        return staticArgs;
    }

    public void setStaticargs(String staticArgs) {
        this.staticArgs = staticArgs;
    }
    public String getTargetplatform() {
        return targetPlatform;
    }

    public void setTargetplatform(String targetPlatform) {
        this.targetPlatform = targetPlatform;
    }
    public String getTargets() {
        return targets;
    }

    public void setTargets(String targets) {
        this.targets = targets;
    }
    public String getOutputargs() {
        return outputArgs;
    }

    public void setOutputargs(String outputArgs) {
        this.outputArgs = outputArgs;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public easyflow_EasyFlowMetadata getEasyflow_easyflowmetadata() {
        return easyflow_easyflowmetadata;
    }

    public void setEasyflow_easyflowmetadata(easyflow_EasyFlowMetadata easyflow_easyflowmetadata) {
        this.easyflow_easyflowmetadata = easyflow_easyflowmetadata;
    }

}