





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsElement  {

    private String name;
    private String description;
    private String fullName;
    private String sqlName;
    private String originalName;
    private String uuid;
    private String originalPackage;
    private String shortName;



    public rdbms_RdbmsElement(
        String name,        String description,        String fullName,        String sqlName,        String originalName,        String uuid,        String originalPackage,        String shortName    ) {
        this.name = name;
        this.description = description;
        this.fullName = fullName;
        this.sqlName = sqlName;
        this.originalName = originalName;
        this.uuid = uuid;
        this.originalPackage = originalPackage;
        this.shortName = shortName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getSqlname() {
        return sqlName;
    }

    public void setSqlname(String sqlName) {
        this.sqlName = sqlName;
    }
    public String getOriginalname() {
        return originalName;
    }

    public void setOriginalname(String originalName) {
        this.originalName = originalName;
    }
    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public String getOriginalpackage() {
        return originalPackage;
    }

    public void setOriginalpackage(String originalPackage) {
        this.originalPackage = originalPackage;
    }
    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }


}