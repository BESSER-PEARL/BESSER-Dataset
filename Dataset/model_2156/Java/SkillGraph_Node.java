





import java.util.List;
import java.util.ArrayList;

public class SkillGraph_Node  {

    private String programPath;
    private String name;
    private String category;





    private SkillGraph_Node skillgraph_node;




    private SkillGraph_Edge skillgraph_edge;




    private SkillGraph_Requirement skillgraph_requirement;




    private List<SkillGraph_Edge> skillgraph_edges;




    private SkillGraph_Graph skillgraph_graph;




    private List<SkillGraph_Equation> skillgraph_equations;




    private SkillGraph_Edge skillgraph_edge;




    private SkillGraph_Graph skillgraph_graph;




    private List<SkillGraph_Requirement> skillgraph_requirements;




    private SkillGraph_Equation skillgraph_equation;


    public SkillGraph_Node(
        String programPath,        String name,        String category    ) {
        this.programPath = programPath;
        this.name = name;
        this.category = category;
        this.skillgraph_edges = new ArrayList<>();
        this.skillgraph_equations = new ArrayList<>();
        this.skillgraph_requirements = new ArrayList<>();
    }

    public SkillGraph_Node(
        String programPath,        String name,        String category        ArrayList<SkillGraph_Edge> skillgraph_edges,        ArrayList<SkillGraph_Equation> skillgraph_equations,        ArrayList<SkillGraph_Requirement> skillgraph_requirements    ) {
        this.programPath = programPath;
        this.name = name;
        this.category = category;
        this.skillgraph_edges = skillgraph_edges;
        this.skillgraph_equations = skillgraph_equations;
        this.skillgraph_requirements = skillgraph_requirements;
    }

    public String getProgrampath() {
        return programPath;
    }

    public void setProgrampath(String programPath) {
        this.programPath = programPath;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public SkillGraph_Node getSkillgraph_node() {
        return skillgraph_node;
    }

    public void setSkillgraph_node(SkillGraph_Node skillgraph_node) {
        this.skillgraph_node = skillgraph_node;
    }
    public SkillGraph_Edge getSkillgraph_edge() {
        return skillgraph_edge;
    }

    public void setSkillgraph_edge(SkillGraph_Edge skillgraph_edge) {
        this.skillgraph_edge = skillgraph_edge;
    }
    public SkillGraph_Requirement getSkillgraph_requirement() {
        return skillgraph_requirement;
    }

    public void setSkillgraph_requirement(SkillGraph_Requirement skillgraph_requirement) {
        this.skillgraph_requirement = skillgraph_requirement;
    }
    public List<SkillGraph_Edge> getSkillgraph_edges() {
        return skillgraph_edges;
    }

    public void addSkillgraph_edge(Skillgraph_edge skillgraph_edge) {
        this.skillgraph_edges.add(skillgraph_edge);
    }
    public SkillGraph_Graph getSkillgraph_graph() {
        return skillgraph_graph;
    }

    public void setSkillgraph_graph(SkillGraph_Graph skillgraph_graph) {
        this.skillgraph_graph = skillgraph_graph;
    }
    public List<SkillGraph_Equation> getSkillgraph_equations() {
        return skillgraph_equations;
    }

    public void addSkillgraph_equation(Skillgraph_equation skillgraph_equation) {
        this.skillgraph_equations.add(skillgraph_equation);
    }
    public SkillGraph_Edge getSkillgraph_edge() {
        return skillgraph_edge;
    }

    public void setSkillgraph_edge(SkillGraph_Edge skillgraph_edge) {
        this.skillgraph_edge = skillgraph_edge;
    }
    public SkillGraph_Graph getSkillgraph_graph() {
        return skillgraph_graph;
    }

    public void setSkillgraph_graph(SkillGraph_Graph skillgraph_graph) {
        this.skillgraph_graph = skillgraph_graph;
    }
    public List<SkillGraph_Requirement> getSkillgraph_requirements() {
        return skillgraph_requirements;
    }

    public void addSkillgraph_requirement(Skillgraph_requirement skillgraph_requirement) {
        this.skillgraph_requirements.add(skillgraph_requirement);
    }
    public SkillGraph_Equation getSkillgraph_equation() {
        return skillgraph_equation;
    }

    public void setSkillgraph_equation(SkillGraph_Equation skillgraph_equation) {
        this.skillgraph_equation = skillgraph_equation;
    }

}