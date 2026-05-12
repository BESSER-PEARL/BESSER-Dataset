





import java.util.List;
import java.util.ArrayList;

public class build_Build  {

    private String time;
    private String date;
    private String label;
    private String buildRoot;
    private String type;
    private String builderURL;
    private String launchVM;
    private String fetchTag;
    private boolean sendmail;





    private build_Promotion build_promotion;




    private build_Product build_product;




    private build_Contact build_contact;




    private build_Compiler build_compiler;




    private build_Map build_map;




    private List<build_Category> build_categorys;




    private List<build_Platform> build_platforms;




    private List<build_Contact> build_contacts;




    private build_Platform build_platform;




    private List<build_Config> build_configs;




    private build_Platform build_platform;




    private List<build_Contribution> build_contributions;


    public build_Build(
        String time,        String date,        String label,        String buildRoot,        String type,        String builderURL,        String launchVM,        String fetchTag,        boolean sendmail    ) {
        this.time = time;
        this.date = date;
        this.label = label;
        this.buildRoot = buildRoot;
        this.type = type;
        this.builderURL = builderURL;
        this.launchVM = launchVM;
        this.fetchTag = fetchTag;
        this.sendmail = sendmail;
        this.build_categorys = new ArrayList<>();
        this.build_platforms = new ArrayList<>();
        this.build_contacts = new ArrayList<>();
        this.build_configs = new ArrayList<>();
        this.build_contributions = new ArrayList<>();
    }

    public build_Build(
        String time,        String date,        String label,        String buildRoot,        String type,        String builderURL,        String launchVM,        String fetchTag,        boolean sendmail        ArrayList<build_Category> build_categorys,        ArrayList<build_Platform> build_platforms,        ArrayList<build_Contact> build_contacts,        ArrayList<build_Config> build_configs,        ArrayList<build_Contribution> build_contributions    ) {
        this.time = time;
        this.date = date;
        this.label = label;
        this.buildRoot = buildRoot;
        this.type = type;
        this.builderURL = builderURL;
        this.launchVM = launchVM;
        this.fetchTag = fetchTag;
        this.sendmail = sendmail;
        this.build_categorys = build_categorys;
        this.build_platforms = build_platforms;
        this.build_contacts = build_contacts;
        this.build_configs = build_configs;
        this.build_contributions = build_contributions;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getBuildroot() {
        return buildRoot;
    }

    public void setBuildroot(String buildRoot) {
        this.buildRoot = buildRoot;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getBuilderurl() {
        return builderURL;
    }

    public void setBuilderurl(String builderURL) {
        this.builderURL = builderURL;
    }
    public String getLaunchvm() {
        return launchVM;
    }

    public void setLaunchvm(String launchVM) {
        this.launchVM = launchVM;
    }
    public String getFetchtag() {
        return fetchTag;
    }

    public void setFetchtag(String fetchTag) {
        this.fetchTag = fetchTag;
    }
    public boolean getSendmail() {
        return sendmail;
    }

    public void setSendmail(boolean sendmail) {
        this.sendmail = sendmail;
    }

    public build_Promotion getBuild_promotion() {
        return build_promotion;
    }

    public void setBuild_promotion(build_Promotion build_promotion) {
        this.build_promotion = build_promotion;
    }
    public build_Product getBuild_product() {
        return build_product;
    }

    public void setBuild_product(build_Product build_product) {
        this.build_product = build_product;
    }
    public build_Contact getBuild_contact() {
        return build_contact;
    }

    public void setBuild_contact(build_Contact build_contact) {
        this.build_contact = build_contact;
    }
    public build_Compiler getBuild_compiler() {
        return build_compiler;
    }

    public void setBuild_compiler(build_Compiler build_compiler) {
        this.build_compiler = build_compiler;
    }
    public build_Map getBuild_map() {
        return build_map;
    }

    public void setBuild_map(build_Map build_map) {
        this.build_map = build_map;
    }
    public List<build_Category> getBuild_categorys() {
        return build_categorys;
    }

    public void addBuild_category(Build_category build_category) {
        this.build_categorys.add(build_category);
    }
    public List<build_Platform> getBuild_platforms() {
        return build_platforms;
    }

    public void addBuild_platform(Build_platform build_platform) {
        this.build_platforms.add(build_platform);
    }
    public List<build_Contact> getBuild_contacts() {
        return build_contacts;
    }

    public void addBuild_contact(Build_contact build_contact) {
        this.build_contacts.add(build_contact);
    }
    public build_Platform getBuild_platform() {
        return build_platform;
    }

    public void setBuild_platform(build_Platform build_platform) {
        this.build_platform = build_platform;
    }
    public List<build_Config> getBuild_configs() {
        return build_configs;
    }

    public void addBuild_config(Build_config build_config) {
        this.build_configs.add(build_config);
    }
    public build_Platform getBuild_platform() {
        return build_platform;
    }

    public void setBuild_platform(build_Platform build_platform) {
        this.build_platform = build_platform;
    }
    public List<build_Contribution> getBuild_contributions() {
        return build_contributions;
    }

    public void addBuild_contribution(Build_contribution build_contribution) {
        this.build_contributions.add(build_contribution);
    }

}