





import java.util.List;
import java.util.ArrayList;

public class HSV2HLS_HSVNode2HLSNode  {

    private String name;
    private String rgb;





    private HSV2HLS_HSVNode2HLSNode hsv2hls_hsvnode2hlsnode;




    private List<HSV2HLS_HSVNode2HLSNode> hsv2hls_hsvnode2hlsnodes;


    public HSV2HLS_HSVNode2HLSNode(
        String name,        String rgb    ) {
        this.name = name;
        this.rgb = rgb;
        this.hsv2hls_hsvnode2hlsnodes = new ArrayList<>();
    }

    public HSV2HLS_HSVNode2HLSNode(
        String name,        String rgb        ArrayList<HSV2HLS_HSVNode2HLSNode> hsv2hls_hsvnode2hlsnodes    ) {
        this.name = name;
        this.rgb = rgb;
        this.hsv2hls_hsvnode2hlsnodes = hsv2hls_hsvnode2hlsnodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRgb() {
        return rgb;
    }

    public void setRgb(String rgb) {
        this.rgb = rgb;
    }

    public HSV2HLS_HSVNode2HLSNode getHsv2hls_hsvnode2hlsnode() {
        return hsv2hls_hsvnode2hlsnode;
    }

    public void setHsv2hls_hsvnode2hlsnode(HSV2HLS_HSVNode2HLSNode hsv2hls_hsvnode2hlsnode) {
        this.hsv2hls_hsvnode2hlsnode = hsv2hls_hsvnode2hlsnode;
    }
    public List<HSV2HLS_HSVNode2HLSNode> getHsv2hls_hsvnode2hlsnodes() {
        return hsv2hls_hsvnode2hlsnodes;
    }

    public void addHsv2hls_hsvnode2hlsnode(Hsv2hls_hsvnode2hlsnode hsv2hls_hsvnode2hlsnode) {
        this.hsv2hls_hsvnode2hlsnodes.add(hsv2hls_hsvnode2hlsnode);
    }

}