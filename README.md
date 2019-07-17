# tempy - project template for Python
tempy is a OPINIONATED project template for Python (currently for Windows).

## Opinions
* (x pyenv)
* pipenv
* VSCode  
* black
  
## Before project start
### venvディレクトリパス
```
（環境変数）
PIPENV_VENV_IN_PROJECT: true  
```
venvディレクトリをプロジェクト内に配置できる (node_modulesと同等)  
[reference](https://pipenv.readthedocs.io/en/latest/advanced/#pipenv.environments.PIPENV_VENV_IN_PROJECT)  

利点は2つ  

* 依存ライブラリの削除が容易（プロジェクト削除、依存手動リセット）
* エディタに優しい（小並感）（デバッガがvenvを実行環境として暗示的に利用しやすい）

## Project start
### fork tempy
```
git clone https://github.com/tarepan/tempy.git
```

### start venv
```
pipenv --python <version e.g. 3.7>
```

### change name
tempy => packagename (all lower-case, without underscore (PEP8))  

### reset git
delete .git manually

## During project
### Type Checking
[Pyright](https://github.com/microsoft/pyright)  
For simplicity, tempy suggests VSCode extension (Pyright has also CLI).  

Disadvantage of CLI  

- needs npm
  - plan A: specify Pyright version explicitly in package.json (extra file in project)
  - plan B: use Pyright implicitly with npm install -g (version not under control)

### Linting
### Formatting
Black
### Execution
F5 of VSCode