





import java.util.List;
import java.util.ArrayList;

public class gama_ELayer extends EGamaObject {

    private String type;
    private String isColorCst;
    private String color;
    private String file;
    private String species;
    private String colorRBG;
    private String grid;
    private String aspect;
    private boolean showLines;
    private String size;
    private String agents;
    private String chart_type;
    private String text;
    private String gamlCode;





    private gama_EDisplay gama_edisplay;




    private List<gama_EChartLayer> gama_echartlayers;




    private gama_EDisplay gama_edisplay;


    public gama_ELayer(
        String type,        String isColorCst,        String color,        String file,        String species,        String colorRBG,        String grid,        String aspect,        boolean showLines,        String size,        String agents,        String chart_type,        String text,        String gamlCode    ) {
        super(
        );
        this.type = type;
        this.isColorCst = isColorCst;
        this.color = color;
        this.file = file;
        this.species = species;
        this.colorRBG = colorRBG;
        this.grid = grid;
        this.aspect = aspect;
        this.showLines = showLines;
        this.size = size;
        this.agents = agents;
        this.chart_type = chart_type;
        this.text = text;
        this.gamlCode = gamlCode;
        this.gama_echartlayers = new ArrayList<>();
    }

    public gama_ELayer(
        String type,        String isColorCst,        String color,        String file,        String species,        String colorRBG,        String grid,        String aspect,        boolean showLines,        String size,        String agents,        String chart_type,        String text,        String gamlCode        ArrayList<gama_EChartLayer> gama_echartlayers    ) {
        this.type = type;
        this.isColorCst = isColorCst;
        this.color = color;
        this.file = file;
        this.species = species;
        this.colorRBG = colorRBG;
        this.grid = grid;
        this.aspect = aspect;
        this.showLines = showLines;
        this.size = size;
        this.agents = agents;
        this.chart_type = chart_type;
        this.text = text;
        this.gamlCode = gamlCode;
        this.gama_echartlayers = gama_echartlayers;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIscolorcst() {
        return isColorCst;
    }

    public void setIscolorcst(String isColorCst) {
        this.isColorCst = isColorCst;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }
    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }
    public String getColorrbg() {
        return colorRBG;
    }

    public void setColorrbg(String colorRBG) {
        this.colorRBG = colorRBG;
    }
    public String getGrid() {
        return grid;
    }

    public void setGrid(String grid) {
        this.grid = grid;
    }
    public String getAspect() {
        return aspect;
    }

    public void setAspect(String aspect) {
        this.aspect = aspect;
    }
    public boolean getShowlines() {
        return showLines;
    }

    public void setShowlines(boolean showLines) {
        this.showLines = showLines;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getAgents() {
        return agents;
    }

    public void setAgents(String agents) {
        this.agents = agents;
    }
    public String getChart_type() {
        return chart_type;
    }

    public void setChart_type(String chart_type) {
        this.chart_type = chart_type;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getGamlcode() {
        return gamlCode;
    }

    public void setGamlcode(String gamlCode) {
        this.gamlCode = gamlCode;
    }

    public gama_EDisplay getGama_edisplay() {
        return gama_edisplay;
    }

    public void setGama_edisplay(gama_EDisplay gama_edisplay) {
        this.gama_edisplay = gama_edisplay;
    }
    public List<gama_EChartLayer> getGama_echartlayers() {
        return gama_echartlayers;
    }

    public void addGama_echartlayer(Gama_echartlayer gama_echartlayer) {
        this.gama_echartlayers.add(gama_echartlayer);
    }
    public gama_EDisplay getGama_edisplay() {
        return gama_edisplay;
    }

    public void setGama_edisplay(gama_EDisplay gama_edisplay) {
        this.gama_edisplay = gama_edisplay;
    }

}