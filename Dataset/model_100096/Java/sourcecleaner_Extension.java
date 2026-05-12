





import java.util.List;
import java.util.ArrayList;

public class sourcecleaner_Extension  {

    private String extra;
    private String id;
    private boolean diagraph;
    private String clazz;
    private String name;
    private String pointId;





    private sourcecleaner_Java sourcecleaner_java;




    private sourcecleaner_Plugin sourcecleaner_plugin;


    public sourcecleaner_Extension(
        String extra,        String id,        boolean diagraph,        String clazz,        String name,        String pointId    ) {
        this.extra = extra;
        this.id = id;
        this.diagraph = diagraph;
        this.clazz = clazz;
        this.name = name;
        this.pointId = pointId;
    }


    public String getExtra() {
        return extra;
    }

    public void setExtra(String extra) {
        this.extra = extra;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getDiagraph() {
        return diagraph;
    }

    public void setDiagraph(boolean diagraph) {
        this.diagraph = diagraph;
    }
    public String getClazz() {
        return clazz;
    }

    public void setClazz(String clazz) {
        this.clazz = clazz;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPointid() {
        return pointId;
    }

    public void setPointid(String pointId) {
        this.pointId = pointId;
    }

    public sourcecleaner_Java getSourcecleaner_java() {
        return sourcecleaner_java;
    }

    public void setSourcecleaner_java(sourcecleaner_Java sourcecleaner_java) {
        this.sourcecleaner_java = sourcecleaner_java;
    }
    public sourcecleaner_Plugin getSourcecleaner_plugin() {
        return sourcecleaner_plugin;
    }

    public void setSourcecleaner_plugin(sourcecleaner_Plugin sourcecleaner_plugin) {
        this.sourcecleaner_plugin = sourcecleaner_plugin;
    }

}