




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class web_Release  {

    private LocalDate date;
    private String releaseNotesLink;
    private String unqualifiedName;
    private String type;
    private boolean javadoc;
    private String baseName;
    private String alternateMsiName;
    private String name;
    private String buildId;





    private web_Version web_version;




    private web_ReleaseSection web_releasesection;




    private web_Version web_version;


    public web_Release(
        LocalDate date,        String releaseNotesLink,        String unqualifiedName,        String type,        boolean javadoc,        String baseName,        String alternateMsiName,        String name,        String buildId    ) {
        this.date = date;
        this.releaseNotesLink = releaseNotesLink;
        this.unqualifiedName = unqualifiedName;
        this.type = type;
        this.javadoc = javadoc;
        this.baseName = baseName;
        this.alternateMsiName = alternateMsiName;
        this.name = name;
        this.buildId = buildId;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getReleasenoteslink() {
        return releaseNotesLink;
    }

    public void setReleasenoteslink(String releaseNotesLink) {
        this.releaseNotesLink = releaseNotesLink;
    }
    public String getUnqualifiedname() {
        return unqualifiedName;
    }

    public void setUnqualifiedname(String unqualifiedName) {
        this.unqualifiedName = unqualifiedName;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getJavadoc() {
        return javadoc;
    }

    public void setJavadoc(boolean javadoc) {
        this.javadoc = javadoc;
    }
    public String getBasename() {
        return baseName;
    }

    public void setBasename(String baseName) {
        this.baseName = baseName;
    }
    public String getAlternatemsiname() {
        return alternateMsiName;
    }

    public void setAlternatemsiname(String alternateMsiName) {
        this.alternateMsiName = alternateMsiName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBuildid() {
        return buildId;
    }

    public void setBuildid(String buildId) {
        this.buildId = buildId;
    }

    public web_Version getWeb_version() {
        return web_version;
    }

    public void setWeb_version(web_Version web_version) {
        this.web_version = web_version;
    }
    public web_ReleaseSection getWeb_releasesection() {
        return web_releasesection;
    }

    public void setWeb_releasesection(web_ReleaseSection web_releasesection) {
        this.web_releasesection = web_releasesection;
    }
    public web_Version getWeb_version() {
        return web_version;
    }

    public void setWeb_version(web_Version web_version) {
        this.web_version = web_version;
    }

}