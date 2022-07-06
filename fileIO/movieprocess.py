f = open("movies.txt", "r")
movie_list = [line.rstrip("\n").split(",") for line in f]
grp_by_year=[movie for movie in movie_list if movie[1]=='2022']
print(len(grp_by_year))

grp_by_lang=[movie for movie in movie_list if movie[-2]=="malayalam"]
print(len(grp_by_lang))

movie_out={}

for movie in movie_list:
    year=movie[1]
    if year in movie_out:
        movie_out[year]+=1
    else:
        movie_out[year]=1
print(movie_out)
print(movie_out.items())
out=max(movie_out.items(),key=lambda ite:ite[1])
print(out)
