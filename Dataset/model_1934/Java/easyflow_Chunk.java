





import java.util.List;
import java.util.ArrayList;

public class easyflow_Chunk  {

    private String tool;
    private String name;
    private String argument;





    private easyflow_StringToChunkMap easyflow_stringtochunkmap;


    public easyflow_Chunk(
        String tool,        String name,        String argument    ) {
        this.tool = tool;
        this.name = name;
        this.argument = argument;
    }


    public String getTool() {
        return tool;
    }

    public void setTool(String tool) {
        this.tool = tool;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getArgument() {
        return argument;
    }

    public void setArgument(String argument) {
        this.argument = argument;
    }

    public easyflow_StringToChunkMap getEasyflow_stringtochunkmap() {
        return easyflow_stringtochunkmap;
    }

    public void setEasyflow_stringtochunkmap(easyflow_StringToChunkMap easyflow_stringtochunkmap) {
        this.easyflow_stringtochunkmap = easyflow_stringtochunkmap;
    }

}