





import java.util.List;
import java.util.ArrayList;

public class qsar_ResourceType  {

    private String name;
    private String type;
    private String uRL;
    private String checksum;
    private String excluded;
    private String no2d;
    private String file;
    private String no3d;
    private String id;
    private String containsErrors;
    private String noMols;





    private qsar_StructurelistType qsar_structurelisttype;


    public qsar_ResourceType(
        String name,        String type,        String uRL,        String checksum,        String excluded,        String no2d,        String file,        String no3d,        String id,        String containsErrors,        String noMols    ) {
        this.name = name;
        this.type = type;
        this.uRL = uRL;
        this.checksum = checksum;
        this.excluded = excluded;
        this.no2d = no2d;
        this.file = file;
        this.no3d = no3d;
        this.id = id;
        this.containsErrors = containsErrors;
        this.noMols = noMols;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }
    public String getChecksum() {
        return checksum;
    }

    public void setChecksum(String checksum) {
        this.checksum = checksum;
    }
    public String getExcluded() {
        return excluded;
    }

    public void setExcluded(String excluded) {
        this.excluded = excluded;
    }
    public String getNo2d() {
        return no2d;
    }

    public void setNo2d(String no2d) {
        this.no2d = no2d;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getNo3d() {
        return no3d;
    }

    public void setNo3d(String no3d) {
        this.no3d = no3d;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getContainserrors() {
        return containsErrors;
    }

    public void setContainserrors(String containsErrors) {
        this.containsErrors = containsErrors;
    }
    public String getNomols() {
        return noMols;
    }

    public void setNomols(String noMols) {
        this.noMols = noMols;
    }

    public qsar_StructurelistType getQsar_structurelisttype() {
        return qsar_structurelisttype;
    }

    public void setQsar_structurelisttype(qsar_StructurelistType qsar_structurelisttype) {
        this.qsar_structurelisttype = qsar_structurelisttype;
    }

}