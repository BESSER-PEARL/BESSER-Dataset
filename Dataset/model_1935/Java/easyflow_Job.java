





import java.util.List;
import java.util.ArrayList;

public class easyflow_Job  {

    private String staticArgs;
    private String targetPlatformOptions;
    private String interpreterOption;
    private String dependencies;
    private String exe;
    private String targets;
    private String name;
    private String source;
    private String targetPlatform;
    private String outputArgs;
    private String genericArgs;
    private String subCmd;
    private String inputArgs;





    private easyflow_EasyFlowMetadata easyflow_easyflowmetadata;


    public easyflow_Job(
        String staticArgs,        String targetPlatformOptions,        String interpreterOption,        String dependencies,        String exe,        String targets,        String name,        String source,        String targetPlatform,        String outputArgs,        String genericArgs,        String subCmd,        String inputArgs    ) {
        this.staticArgs = staticArgs;
        this.targetPlatformOptions = targetPlatformOptions;
        this.interpreterOption = interpreterOption;
        this.dependencies = dependencies;
        this.exe = exe;
        this.targets = targets;
        this.name = name;
        this.source = source;
        this.targetPlatform = targetPlatform;
        this.outputArgs = outputArgs;
        this.genericArgs = genericArgs;
        this.subCmd = subCmd;
        this.inputArgs = inputArgs;
    }


    public String getStaticargs() {
        return staticArgs;
    }

    public void setStaticargs(String staticArgs) {
        this.staticArgs = staticArgs;
    }
    public String getTargetplatformoptions() {
        return targetPlatformOptions;
    }

    public void setTargetplatformoptions(String targetPlatformOptions) {
        this.targetPlatformOptions = targetPlatformOptions;
    }
    public String getInterpreteroption() {
        return interpreterOption;
    }

    public void setInterpreteroption(String interpreterOption) {
        this.interpreterOption = interpreterOption;
    }
    public String getDependencies() {
        return dependencies;
    }

    public void setDependencies(String dependencies) {
        this.dependencies = dependencies;
    }
    public String getExe() {
        return exe;
    }

    public void setExe(String exe) {
        this.exe = exe;
    }
    public String getTargets() {
        return targets;
    }

    public void setTargets(String targets) {
        this.targets = targets;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getTargetplatform() {
        return targetPlatform;
    }

    public void setTargetplatform(String targetPlatform) {
        this.targetPlatform = targetPlatform;
    }
    public String getOutputargs() {
        return outputArgs;
    }

    public void setOutputargs(String outputArgs) {
        this.outputArgs = outputArgs;
    }
    public String getGenericargs() {
        return genericArgs;
    }

    public void setGenericargs(String genericArgs) {
        this.genericArgs = genericArgs;
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

    public easyflow_EasyFlowMetadata getEasyflow_easyflowmetadata() {
        return easyflow_easyflowmetadata;
    }

    public void setEasyflow_easyflowmetadata(easyflow_EasyFlowMetadata easyflow_easyflowmetadata) {
        this.easyflow_easyflowmetadata = easyflow_easyflowmetadata;
    }

}