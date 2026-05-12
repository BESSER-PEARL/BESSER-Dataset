





import java.util.List;
import java.util.ArrayList;

public class StartGame  {

    private int turn;
    private None p4;
    private int bidNumber;
    private None p1;
    private None t1;
    private None p3;
    private None deck;
    private String playerOrder;
    private None t2;
    private None p2;
    private None trick;
    private int lead;





    private List<Trick> tricks;




    private List<Deck> decks;




    private List<Team> teams;




    private List<Player> players;


    public StartGame(
        int turn,        None p4,        int bidNumber,        None p1,        None t1,        None p3,        None deck,        String playerOrder,        None t2,        None p2,        None trick,        int lead    ) {
        this.turn = turn;
        this.p4 = p4;
        this.bidNumber = bidNumber;
        this.p1 = p1;
        this.t1 = t1;
        this.p3 = p3;
        this.deck = deck;
        this.playerOrder = playerOrder;
        this.t2 = t2;
        this.p2 = p2;
        this.trick = trick;
        this.lead = lead;
        this.tricks = new ArrayList<>();
        this.decks = new ArrayList<>();
        this.teams = new ArrayList<>();
        this.players = new ArrayList<>();
    }

    public StartGame(
        int turn,        None p4,        int bidNumber,        None p1,        None t1,        None p3,        None deck,        String playerOrder,        None t2,        None p2,        None trick,        int lead        ArrayList<Trick> tricks,        ArrayList<Deck> decks,        ArrayList<Team> teams,        ArrayList<Player> players    ) {
        this.turn = turn;
        this.p4 = p4;
        this.bidNumber = bidNumber;
        this.p1 = p1;
        this.t1 = t1;
        this.p3 = p3;
        this.deck = deck;
        this.playerOrder = playerOrder;
        this.t2 = t2;
        this.p2 = p2;
        this.trick = trick;
        this.lead = lead;
        this.tricks = tricks;
        this.decks = decks;
        this.teams = teams;
        this.players = players;
    }

    public int getTurn() {
        return turn;
    }

    public void setTurn(int turn) {
        this.turn = turn;
    }
    public None getP4() {
        return p4;
    }

    public void setP4(None p4) {
        this.p4 = p4;
    }
    public int getBidnumber() {
        return bidNumber;
    }

    public void setBidnumber(int bidNumber) {
        this.bidNumber = bidNumber;
    }
    public None getP1() {
        return p1;
    }

    public void setP1(None p1) {
        this.p1 = p1;
    }
    public None getT1() {
        return t1;
    }

    public void setT1(None t1) {
        this.t1 = t1;
    }
    public None getP3() {
        return p3;
    }

    public void setP3(None p3) {
        this.p3 = p3;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public String getPlayerorder() {
        return playerOrder;
    }

    public void setPlayerorder(String playerOrder) {
        this.playerOrder = playerOrder;
    }
    public None getT2() {
        return t2;
    }

    public void setT2(None t2) {
        this.t2 = t2;
    }
    public None getP2() {
        return p2;
    }

    public void setP2(None p2) {
        this.p2 = p2;
    }
    public None getTrick() {
        return trick;
    }

    public void setTrick(None trick) {
        this.trick = trick;
    }
    public int getLead() {
        return lead;
    }

    public void setLead(int lead) {
        this.lead = lead;
    }

    public List<Trick> getTricks() {
        return tricks;
    }

    public void addTrick(Trick trick) {
        this.tricks.add(trick);
    }
    public List<Deck> getDecks() {
        return decks;
    }

    public void addDeck(Deck deck) {
        this.decks.add(deck);
    }
    public List<Team> getTeams() {
        return teams;
    }

    public void addTeam(Team team) {
        this.teams.add(team);
    }
    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }

}