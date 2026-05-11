





import java.util.List;
import java.util.ArrayList;

public class HSV2HLS_HSVNode2HLSNode  {

    private String rgb;
    private String name;





    private HSV2HLS_HSVNode2HLSNode hsv2hls_hsvnode2hlsnode;




    private HSV2HLS_HSVNode hsv2hls_hsvnode;




    private List<HSV2HLS_HSVNode2HLSNode> hsv2hls_hsvnode2hlsnodes;




    private HSV2HLS_HLSNode hsv2hls_hlsnode;


    public HSV2HLS_HSVNode2HLSNode(
        String rgb,        String name    ) {
        this.rgb = rgb;
        this.name = name;
        this.hsv2hls_hsvnode2hlsnodes = new ArrayList<>();
    }

    public HSV2HLS_HSVNode2HLSNode(
        String rgb,        String name        ArrayList<HSV2HLS_HSVNode2HLSNode> hsv2hls_hsvnode2hlsnodes    ) {
        this.rgb = rgb;
        this.name = name;
        this.hsv2hls_hsvnode2hlsnodes = hsv2hls_hsvnode2hlsnodes;
    }

    public String getRgb() {
        return rgb;
    }

    public void setRgb(String rgb) {
        this.rgb = rgb;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public HSV2HLS_HSVNode2HLSNode getHsv2hls_hsvnode2hlsnode() {
        return hsv2hls_hsvnode2hlsnode;
    }

    public void setHsv2hls_hsvnode2hlsnode(HSV2HLS_HSVNode2HLSNode hsv2hls_hsvnode2hlsnode) {
        this.hsv2hls_hsvnode2hlsnode = hsv2hls_hsvnode2hlsnode;
    }
    public HSV2HLS_HSVNode getHsv2hls_hsvnode() {
        return hsv2hls_hsvnode;
    }

    public void setHsv2hls_hsvnode(HSV2HLS_HSVNode hsv2hls_hsvnode) {
        this.hsv2hls_hsvnode = hsv2hls_hsvnode;
    }
    public List<HSV2HLS_HSVNode2HLSNode> getHsv2hls_hsvnode2hlsnodes() {
        return hsv2hls_hsvnode2hlsnodes;
    }

    public void addHsv2hls_hsvnode2hlsnode(Hsv2hls_hsvnode2hlsnode hsv2hls_hsvnode2hlsnode) {
        this.hsv2hls_hsvnode2hlsnodes.add(hsv2hls_hsvnode2hlsnode);
    }
    public HSV2HLS_HLSNode getHsv2hls_hlsnode() {
        return hsv2hls_hlsnode;
    }

    public void setHsv2hls_hlsnode(HSV2HLS_HLSNode hsv2hls_hlsnode) {
        this.hsv2hls_hlsnode = hsv2hls_hlsnode;
    }

}