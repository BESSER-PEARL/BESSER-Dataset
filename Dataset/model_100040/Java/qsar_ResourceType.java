





import java.util.List;
import java.util.ArrayList;

public class qsar_ResourceType  {

    private String name;
    private String no3d;
    private String uRL;
    private String file;
    private String no2d;
    private String checksum;
    private String id;
    private String type;
    private String noMols;
    private String excluded;





    private qsar_StructurelistType qsar_structurelisttype;


    public qsar_ResourceType(
        String name,        String no3d,        String uRL,        String file,        String no2d,        String checksum,        String id,        String type,        String noMols,        String excluded    ) {
        this.name = name;
        this.no3d = no3d;
        this.uRL = uRL;
        this.file = file;
        this.no2d = no2d;
        this.checksum = checksum;
        this.id = id;
        this.type = type;
        this.noMols = noMols;
        this.excluded = excluded;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNo3d() {
        return no3d;
    }

    public void setNo3d(String no3d) {
        this.no3d = no3d;
    }
    public String getUrl() {
        return uRL;
    }

    public void setUrl(String uRL) {
        this.uRL = uRL;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getNo2d() {
        return no2d;
    }

    public void setNo2d(String no2d) {
        this.no2d = no2d;
    }
    public String getChecksum() {
        return checksum;
    }

    public void setChecksum(String checksum) {
        this.checksum = checksum;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getNomols() {
        return noMols;
    }

    public void setNomols(String noMols) {
        this.noMols = noMols;
    }
    public String getExcluded() {
        return excluded;
    }

    public void setExcluded(String excluded) {
        this.excluded = excluded;
    }

    public qsar_StructurelistType getQsar_structurelisttype() {
        return qsar_structurelisttype;
    }

    public void setQsar_structurelisttype(qsar_StructurelistType qsar_structurelisttype) {
        this.qsar_structurelisttype = qsar_structurelisttype;
    }

}