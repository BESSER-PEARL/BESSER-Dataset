




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class web_Release  {

    private boolean javadoc;
    private LocalDate date;
    private String type;
    private String unqualifiedName;
    private String buildId;
    private String releaseNotesLink;
    private String name;
    private String alternateMsiName;





    private web_ReleaseSection web_releasesection;




    private web_Version web_version;




    private web_Version web_version;


    public web_Release(
        boolean javadoc,        LocalDate date,        String type,        String unqualifiedName,        String buildId,        String releaseNotesLink,        String name,        String alternateMsiName    ) {
        this.javadoc = javadoc;
        this.date = date;
        this.type = type;
        this.unqualifiedName = unqualifiedName;
        this.buildId = buildId;
        this.releaseNotesLink = releaseNotesLink;
        this.name = name;
        this.alternateMsiName = alternateMsiName;
    }


    public boolean getJavadoc() {
        return javadoc;
    }

    public void setJavadoc(boolean javadoc) {
        this.javadoc = javadoc;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUnqualifiedname() {
        return unqualifiedName;
    }

    public void setUnqualifiedname(String unqualifiedName) {
        this.unqualifiedName = unqualifiedName;
    }
    public String getBuildid() {
        return buildId;
    }

    public void setBuildid(String buildId) {
        this.buildId = buildId;
    }
    public String getReleasenoteslink() {
        return releaseNotesLink;
    }

    public void setReleasenoteslink(String releaseNotesLink) {
        this.releaseNotesLink = releaseNotesLink;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAlternatemsiname() {
        return alternateMsiName;
    }

    public void setAlternatemsiname(String alternateMsiName) {
        this.alternateMsiName = alternateMsiName;
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
    public web_Version getWeb_version() {
        return web_version;
    }

    public void setWeb_version(web_Version web_version) {
        this.web_version = web_version;
    }

}