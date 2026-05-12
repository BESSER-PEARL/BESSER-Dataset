





import java.util.List;
import java.util.ArrayList;

public class pushbuttonbuild_BuildType  {

    private String testsAreJarred;
    private String jre;
    private String newsgroupPublisherName;
    private String isIncubation;
    private String parentProjectName;
    private String newsgroupPublisherEmail;
    private String shortName;
    private String projectNamespace;



    public pushbuttonbuild_BuildType(
        String testsAreJarred,        String jre,        String newsgroupPublisherName,        String isIncubation,        String parentProjectName,        String newsgroupPublisherEmail,        String shortName,        String projectNamespace    ) {
        this.testsAreJarred = testsAreJarred;
        this.jre = jre;
        this.newsgroupPublisherName = newsgroupPublisherName;
        this.isIncubation = isIncubation;
        this.parentProjectName = parentProjectName;
        this.newsgroupPublisherEmail = newsgroupPublisherEmail;
        this.shortName = shortName;
        this.projectNamespace = projectNamespace;
    }


    public String getTestsarejarred() {
        return testsAreJarred;
    }

    public void setTestsarejarred(String testsAreJarred) {
        this.testsAreJarred = testsAreJarred;
    }
    public String getJre() {
        return jre;
    }

    public void setJre(String jre) {
        this.jre = jre;
    }
    public String getNewsgrouppublishername() {
        return newsgroupPublisherName;
    }

    public void setNewsgrouppublishername(String newsgroupPublisherName) {
        this.newsgroupPublisherName = newsgroupPublisherName;
    }
    public String getIsincubation() {
        return isIncubation;
    }

    public void setIsincubation(String isIncubation) {
        this.isIncubation = isIncubation;
    }
    public String getParentprojectname() {
        return parentProjectName;
    }

    public void setParentprojectname(String parentProjectName) {
        this.parentProjectName = parentProjectName;
    }
    public String getNewsgrouppublisheremail() {
        return newsgroupPublisherEmail;
    }

    public void setNewsgrouppublisheremail(String newsgroupPublisherEmail) {
        this.newsgroupPublisherEmail = newsgroupPublisherEmail;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }
    public String getProjectnamespace() {
        return projectNamespace;
    }

    public void setProjectnamespace(String projectNamespace) {
        this.projectNamespace = projectNamespace;
    }


}