





import java.util.List;
import java.util.ArrayList;

public class HLSTree_HLSNode  {

    private String hls;
    private String name;





    private HLSTree_HLSNode hlstree_hlsnode;




    private List<HLSTree_HLSNode> hlstree_hlsnodes;


    public HLSTree_HLSNode(
        String hls,        String name    ) {
        this.hls = hls;
        this.name = name;
        this.hlstree_hlsnodes = new ArrayList<>();
    }

    public HLSTree_HLSNode(
        String hls,        String name        ArrayList<HLSTree_HLSNode> hlstree_hlsnodes    ) {
        this.hls = hls;
        this.name = name;
        this.hlstree_hlsnodes = hlstree_hlsnodes;
    }

    public String getHls() {
        return hls;
    }

    public void setHls(String hls) {
        this.hls = hls;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public HLSTree_HLSNode getHlstree_hlsnode() {
        return hlstree_hlsnode;
    }

    public void setHlstree_hlsnode(HLSTree_HLSNode hlstree_hlsnode) {
        this.hlstree_hlsnode = hlstree_hlsnode;
    }
    public List<HLSTree_HLSNode> getHlstree_hlsnodes() {
        return hlstree_hlsnodes;
    }

    public void addHlstree_hlsnode(Hlstree_hlsnode hlstree_hlsnode) {
        this.hlstree_hlsnodes.add(hlstree_hlsnode);
    }

}